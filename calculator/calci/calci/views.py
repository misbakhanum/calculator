from django .shortcuts import render;
def calculator(request):
    result= None
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        sign = request.POST.get("sign")
        try:
            num1 = float(num1)
            num2 = float(num2)

            if sign == "+":
                result = num1 + num2
            elif sign == "-":
                result = num1 - num2
            elif sign == "*":
                result = num1 * num2
            elif sign == "/":
                result == num1 / num2
            else:
                result = "Invalid sign"
        except ValueError:
            result = "Invalid input"
        return render(request, "calculator.html", {"result": result})
    return render(request, "calculator.html")