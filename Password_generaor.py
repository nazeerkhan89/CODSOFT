import random
import string
import argparse
import sys

class PasswordGenerator:
    def __init__(self):
        self.char_sets = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'digits': string.digits,
            'special': string.punctuation
        }
    
    def generate_password(self, length=12, complexity='medium'):
        """
        Generate a random password based on specified length and complexity.
        
        Args:
            length (int): Length of the password (default: 12)
            complexity (str): Complexity level ('low', 'medium', 'high')
            
        Returns:
            str: Generated password
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Define character pool based on complexity
        if complexity == 'low':
            char_pool = self.char_sets['lower'] + self.char_sets['digits']
        elif complexity == 'medium':
            char_pool = (self.char_sets['lower'] + self.char_sets['upper'] + 
                        self.char_sets['digits'])
        elif complexity == 'high':
            char_pool = (self.char_sets['lower'] + self.char_sets['upper'] + 
                        self.char_sets['digits'] + self.char_sets['special'])
        else:
            raise ValueError("Invalid complexity level. Choose 'low', 'medium', or 'high'")
        
        # Ensure at least one character from each selected set
        password = []
        if complexity == 'low':
            password.append(random.choice(self.char_sets['lower']))
            password.append(random.choice(self.char_sets['digits']))
        elif complexity == 'medium':
            password.append(random.choice(self.char_sets['lower']))
            password.append(random.choice(self.char_sets['upper']))
            password.append(random.choice(self.char_sets['digits']))
        elif complexity == 'high':
            password.append(random.choice(self.char_sets['lower']))
            password.append(random.choice(self.char_sets['upper']))
            password.append(random.choice(self.char_sets['digits']))
            password.append(random.choice(self.char_sets['special']))
        
        # Fill the rest with random characters
        remaining_length = length - len(password)
        password.extend(random.choices(char_pool, k=remaining_length))
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password)
        
        return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('-l', '--length', type=int, default=12,
                       help='Length of the password (default: 12)')
    parser.add_argument('-c', '--complexity', type=str, default='medium',
                       choices=['low', 'medium', 'high'],
                       help='Complexity level (low, medium, high)')
    parser.add_argument('-g', '--gui', action='store_true',
                       help='Launch in GUI mode (if implemented)')
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    try:
        password = generator.generate_password(args.length, args.complexity)
        print("\nGenerated Password:")
        print("-" * 20)
        print(password)
        print("-" * 20)
        print(f"Length: {len(password)} characters")
        print(f"Complexity: {args.complexity}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
