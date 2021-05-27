# Este programa realiza el proceso de expansión binaria
# de Neal Koblitz útil para los algoritmos de codificación
# De Shannon y relativos.

from fractions import Fraction as frac

def algorithm():
    double = list()
    binaryDigit = list()

    rTop = int(input("Numerador: "))
    rBot = int(input("Denominador: "))

    r = frac(rTop, rBot)

    double.append(frac(r * 2))

    for num in double:
        if(num >= 1):
            nextAppend = frac((num - 1)) * 2
            if(nextAppend in double):
                double.append(frac(nextAppend))
                binaryDigit.append(1)
                return(double, binaryDigit)
            double.append(frac(nextAppend))
            binaryDigit.append(1)
        else:
            nextAppend = frac(num) * 2
            if(nextAppend in double):
                double.append(frac(nextAppend))
                binaryDigit.append(0)
                return(double, binaryDigit)
            double.append(frac(nextAppend))
            binaryDigit.append(0)
            
print("([Double after adjustment], [Binary digit]):", algorithm())
