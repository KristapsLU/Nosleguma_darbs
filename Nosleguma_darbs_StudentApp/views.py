from django.shortcuts import render
from Nosleguma_darbs_StudentApp.models import StudentModel

def add_student(request):
    from Nosleguma_darbs_StudentApp.forms import AddStudentForm
    from Nosleguma_darbs_StudentApp.Klase import Student
    form = AddStudentForm(request.POST or None)

    if form.is_valid():
        new_student = Student(form.cleaned_data['name'],
                              form.cleaned_data['grades'])

        student_tosave = StudentModel(name=new_student.name,
                                      grades=new_student.grades,
                                      average_grade=new_student.average_grade)
        student_tosave.save()

        context = {
            'student': student_tosave
        }

        return render(request,
                      template_name='student.html',
                      context=context)

    context = {
        'form': form,
    }

    return render(request,
                  template_name='add_student.html',
                  context=context)


def get_all_students(request):
    context = {
        'students': StudentModel.objects.all()
    }

    return render(request,
                  template_name='all_students.html',
                  context=context)


def get_student(request, student_id):
    context = {
        'student': StudentModel.objects.get(id=student_id)
    }

    return render(request,
                  template_name='student.html',
                  context=context)
