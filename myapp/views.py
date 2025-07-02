from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Create or List Students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_list.html', {'students': students})

# Add New Student
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'myapp/student_form.html', {'form': form})

# Update Student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'myapp/student_form.html', {'form': form})

# Delete Student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'myapp/student_confirm_delete.html', {'student': student})
