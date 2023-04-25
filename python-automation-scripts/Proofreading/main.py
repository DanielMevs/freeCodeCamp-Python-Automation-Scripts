from proofread import proofread

with open('sample_text.txt', 'r') as f:
    lines = f.readlines()
    new_lines = ''
    for row in lines:
        new_lines += row


proofread(new_lines)




