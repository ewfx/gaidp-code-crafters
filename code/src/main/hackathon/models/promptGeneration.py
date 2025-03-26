def append_file_contents_to_prompt(prompt_file, instructions_file, columns_file, output_file):
    with open(instructions_file, 'r') as file:
        instructions_content = file.read()
    
    with open(columns_file, 'r') as file:
        columns_content = file.read()
    
    with open(prompt_file, 'r') as file:
        prompt_content = file.read()
    
    with open(output_file, 'w') as file:
        file.write(prompt_content)
        file.write("\nInstructions file: sample-inst.txt\n")
        file.write(instructions_content)
        file.write("\nColumn descriptions file: col-desc.txt\n")
        file.write(columns_content)
    return