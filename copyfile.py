import shutil

# Define the source HTML file
src_file = 'myLessonPlan.html'

# Loop through a range of numbers from 1 to 8
for i in range(1, 2):
    # Define the destination file name with a suffix
    dest_file = 'project_' + str(i) + '.html'
    # Copy the source file to the destination file
    shutil.copy(src_file, dest_file)
