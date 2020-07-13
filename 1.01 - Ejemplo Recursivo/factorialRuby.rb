#Comment by Line
/

Comment multiple Line

/

def factorial n
    if n<2
        return 1
    end
    n*factorial(n-1)
end

n = 5
puts( "El factorial de %d es %d" % [n, factorial(n)] )