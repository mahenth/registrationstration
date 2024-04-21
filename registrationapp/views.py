

# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student
from django.shortcuts import render, redirect, get_object_or_404

# This is the main view for the home page of the application
def home(request):
    # Render the home.html template when the home view is accessed
    return render(request, 'home.html')

# This view handles the display and processing of the student registration form
def registration_form(request):
    # If the request method is POST, create a new Student instance from the form data
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the list of registered students after successful form submission
            return redirect('registered_students')
    else:
        # If the request method is not POST, create an empty StudentRegistrationForm
        form = StudentRegistrationForm()
    # Render the registration_form.html template with the form
    return render(request, 'registration_form.html', {'form': form})

# This view displays the list of registered students, with optional filtering by name, year, or department
def registered_students(request):
    # Get query parameters for filtering
    query = request.GET.get('q')
    year_filter = request.GET.get('year')
    department_filter = request.GET.get('department')
    # Get all Student instances
    students = Student.objects.all()

    # If a query parameter is present, filter the students queryset by first_name or last_name
    if query:
        students = students.filter(first_name__icontains=query) | students.filter(last_name__icontains=query)
    
    # If a year filter is present, filter the students queryset by year
    if year_filter:
        students = students.filter(year=year_filter)
    
    # If a department filter is present, filter the students queryset by department
    if department_filter:
        students = students.filter(department=department_filter)

    # Render the registered_students.html template with the filtered students queryset and query parameter
    return render(request, 'registered_students.html', {'students': students, 'query': query})

# This view handles the editing of a student instance
def edit_student(request, student_id):
    # Get the student instance by its ID
    student = get_object_or_404(Student, id=student_id)

    # If the request method is POST, update the student instance with the form data
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # Redirect to the list of registered students after successful form submission
            return redirect('registered_students')
    else:
        # If the request method is not POST, create a StudentRegistrationForm instance with the student instance
        form = StudentRegistrationForm(instance=student)
    # Render the edit_student.html template with the form
    return render(request, 'edit_student.html', {'form': form})

# This view handles the deletion of a student instance
def delete_student(request, student_id):
    # Get the student instance by its ID
    student = get_object_or_404(Student, id=student_id)
    
    # If the request method is POST, delete the student instance
    if request.method == 'POST':
        student.delete()
        # Redirect to the list of registered students after successful form submission
        return redirect('registered_students')
    
    # Render the delete_student.html template with the student instance
    return render(request, 'delete_student.html', {'student': student})