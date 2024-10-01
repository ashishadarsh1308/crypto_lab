def letter_grades(highest):
    failing_threshold = 40
    
    num_intervals = 4
    
    score_range = highest - failing_threshold
    
    step = score_range // num_intervals
    
    thresholds = [failing_threshold + step * i + 1 for i in range(1, num_intervals + 1)]
    
    return thresholds

# Test the function
print(letter_grades(100))  
print(letter_grades(88)) 
