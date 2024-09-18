import argparse
import wikipedia
import os
import re

def wiki_to_markdown(topic):
    try:
        # Fetch the Wikipedia page
        page = wikipedia.page(topic)
        
        # Convert content to markdown
        content = "# " + page.title + "\n"
        content += page.content
        content = re.sub(r'(=+)\s*(.+?)\s*\1', lambda m: '#' * len(m.group(1)) + ' ' + m.group(2), content)
        
        # Get references
        references = page.references
        
        # Add references to the markdown content
        content += "\n"
        for ref in references:
            content += f"- {ref}\n"
        
        # Save to file
        # Check if output folder exists, if not create one
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        output_file = os.path.join(output_folder, f"{topic}.md")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Markdown file saved as {output_file}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguous topic. Possible matches are: {e.options}")
    except wikipedia.exceptions.PageError:
        print(f"Page for '{topic}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Convert Wikipedia page to Markdown")
    parser.add_argument("--topic", required=True, help="Wikipedia topic or page title")
    
    args = parser.parse_args()
    
    wiki_to_markdown(args.topic)

if __name__ == "__main__":
    main()
