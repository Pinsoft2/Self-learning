import csv
import sys


def main():

    # TODO: Check for command-line usage
    try:
        if len(sys.argv) != 3:
            raise ValueError("Missing command-line argument")
    # load csv file as standard DNA library
        library = []
        with open(sys.argv[1]) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                library.append(row)

# TODO: Read DNA sequence file into a variable
        with open(sys.argv[2]) as txt_file:
            sequence = txt_file.read()


# TODO: Find longest match of each STR in DNA sequence
        match = {}
        csv_str_sequences = list(library[0].keys())[1:]      # all dna combo from cvs file

        for csv_sub_sequences in csv_str_sequences:
            longest_run = longest_match(sequence, csv_sub_sequences)
            match[csv_sub_sequences] = longest_run


    # # TODO: Check database for matching profiles
        found_match = False
        for person in library:
            matches_all = True
            # Compare each STR count
            for str_name in csv_str_sequences:
                if person[str_name] != str(match[str_name]):
                    matches_all = False
                    break

            if matches_all:
                print(person['name'])
                found_match = True
                break

        if not found_match:
            print("No match")


    except FileNotFoundError:
        sys.exit("File not found")
    except ValueError as e:
        sys.exit(f"An error occurred: {e}")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
