def factorial(targetnumber):
    #base function
    if targetnumber==1:
        return 1
    # Recursive Case
    else:
        return(targetnumber*factorial(targetnumber-1))
        """
        The memory is allocated on stacks. The memory is added/removed in LIFO process.
        # Step1 : return(5*factorial(4))
        # Step2:  return(4*factorial(3))
        # Step3:  return(3*factorial(2))
        # Step4:  return(2*factorial(1))
        # Step5:  targetnumber==1 - return 1
        """



print(factorial(5))

