
def calculate_average (backend,frontend,design):
    return (backend+frontend+design)/3

    
def get_avarage_marks(average):
    if(average>=80):
        return("A")
    elif(average>=70):
        return("B")
    elif(average>=60):
        return("C")
    elif(average>=50):
        return("D")
    else:
        return "E"
    

def student_report(name, frontend, design, backend):
    average=calculate_average(backend,frontend,design)
    grade=get_avarage_marks(average)
    return {
        'name':name,
        'frontend':frontend,
        'design':design,
        'average':average,
        'grade':grade,

    }




name= input("Enter your name: ")
backend=int(input("Enter your Backend marks: "))
frontend=int(input("Enter your Frontend  marks: "))
design=int(input("Enter your Design marks: "))

print(student_report(name,frontend,design,backend))


