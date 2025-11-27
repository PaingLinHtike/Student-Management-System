from django.shortcuts import render, redirect
from django.http import HttpResponse
import pymongo
from bson.objectid import ObjectId

# -----------------------------
#   MongoDB CONNECTION
# -----------------------------
client = pymongo.MongoClient("localhost", 27017)
db = client["Student_Management_System"]
collection = db["student_list"]


# -----------------------------
#   LIST STUDENTS
# -----------------------------
def student_list(request):
    students_cursor = collection.find()
    students = []
    for student in students_cursor:
        student["id"] = str(student["_id"])
        students.append(student)
    return render(request, "student_list/student_list.html", {"students": students})


# -----------------------------
#   CREATE STUDENT
# -----------------------------
def create_student(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "gender": request.POST.get("gender"),
            "phone": request.POST.get("phone")
        }
        collection.insert_one(data)
        return redirect("student_list")

    return render(request, "student_list/create_student.html")


# -----------------------------
#   EDIT STUDENT
# -----------------------------
def edit_student(request, id):
    student = collection.find_one({"_id": ObjectId(id)})
    student["id"] = str(student["_id"])

    if request.method == "POST":
        collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "gender": request.POST.get("gender"),
                "phone": request.POST.get("phone")
            }}
        )
        return redirect("student_list")

    return render(request, "student_list/edit_student.html", {"student": student})


# -----------------------------
#   DELETE STUDENT
# -----------------------------
# -----------------------------
#   DELETE STUDENT
# -----------------------------
def delete_student(request, id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect("student_list")
