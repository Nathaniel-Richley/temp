while True: 
   temperature = float(input("Enter your temperature: "))

   def convert_temperature():
       global temperature
       temperature = float(input("Enter your temperature: "))
   unit = input("F or C? ")

   if unit.upper() == "F":
     converted_temp = (temperature - 32) * 5/9
     print(f"{temperature}°F is {converted_temp:.2f}°C")
   elif unit.upper() == 'C':
     converted_temp = (temperature * 9/5) + 32
     print(f"{temperature}°C is {converted_temp:.2f}°F")
   else:
     print("Please enter 'F' or 'C'.")

   convert_temperature()