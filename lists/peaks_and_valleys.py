"""
# Returns the indices of peaks. A peak has a lower number on both the left and the right.
>>> peaks([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9])
[6, 14]


# Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
>>> valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9])
[9, 17]


# Returns a list with the indices of both peaks and valleys
>>> peaks_and_valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9])
[6, 9, 14, 17]


# Uses the peak and valley indices to return a list of lists, each containing the values of a slope.
>>> chop([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9], [6, 9, 14, 19])
[[1, 2, 3, 4, 5, 6, 7], [6, 5, 4], [5, 6, 7, 8, 9], [8, 7, 6], [7, 8, 9]]

"""

def peaks(sample_list):
    output_list = list()

    for i, num in enumerate(sample_list):
        if sample_list[i+1] < num and sample_list[i-1] < num:
            output_list.append(i)

        return output

def valleys(sample_list):
    output_list = list()

    for i, num in enumerate(sample_list):
        if sample_list[i+1] > num and sample_list[i-1] > num:
            output_list.append(i)

        return output

def peaks_and_valleys(sample_list):

    output_list =list()

    output_list.extend(peaks(sample_list) + valleys(sample_list))

    return sorted(output_list, key=abs)

def chop(sample_list):
#Needs to be finished.
