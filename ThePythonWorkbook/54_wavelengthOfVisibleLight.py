# assigning a wavelength given in [nm]to a colour or through error if out of range

wavelengthOfInterest = int(input("Please give the wavelength in nm: "))

if wavelengthOfInterest >= 380 and wavelengthOfInterest < 450:
    print(wavelengthOfInterest, "nm is violet")
elif wavelengthOfInterest >= 450 and wavelengthOfInterest < 495:
    print(wavelengthOfInterest, "nm is blue")
elif wavelengthOfInterest >= 495 and wavelengthOfInterest < 570:
    print(wavelengthOfInterest, "nm is green")
elif wavelengthOfInterest >= 570 and wavelengthOfInterest < 590:
    print(wavelengthOfInterest, "nm is yellow")
elif wavelengthOfInterest >= 590 and wavelengthOfInterest < 620:
    print(wavelengthOfInterest, "nm is orange")
elif wavelengthOfInterest >= 620 and wavelengthOfInterest < 750:
    print(wavelengthOfInterest, "nm is red")
else:
    print(wavelengthOfInterest, "is out of visible light range")
