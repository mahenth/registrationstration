from django.urls import path
from. import views

# Define the URL patterns for the application
urlpatterns = [
    # Map the root URL to the home view
    path('', views.home, name='home'),
    # Map the 'registration_form' URL to the registration_form view
    path('registration_form', views.registration_form, name='registration_form'),
    # Map the 'registered-students/' URL to the registered_students view
    path('registered-students/', views.registered_students, name='registered_students'),
    # Map the 'edit-student/<int:student_id>/' URL to the edit_student view
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    # Map the 'delete-student/<int:student_id>/' URL to the delete_student view
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
]