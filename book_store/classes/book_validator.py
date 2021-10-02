class Books:
    def __init__(self,author,book_title,number_of_chapters,number_of_pages,publication_date,creation_date):
        """
        Initializing artist, song, and album.
        """
        self.author = author
        self.book_title = book_title
        self.number_of_chapters = number_of_chapters
        self.number_of_pages = number_of_pages
        self.publication_date = publication_date
        self.creation_date = creation_date
    def validate_author(self,author):
        """
        Creating a method that takes an artist name as
        arguments and validates it.

        The method checks to see if the length of an artist is
        greater than 0 and ensures that all character values
        are either numbers or letters.
        """
        if (("-" in author) and (author.replace('-','')).isalnum()) or (("." in author) and (author.replace('.','')).isalnum()) or (("'" in author) and (author.replace("'","'")).isalnum()) or author.isalnum() :
            return True
        else:
            print(f"Sorry, but \'{author}\', is invalid! Please try again!")
            return False
    def validate_booktitle(self,booktitle):
        """
        Creating a method that accepts the name of an
        album and validates it.

        The method checks to see if the length of the 
        album name entered is greater than 0 character values.
        It then goes to check if the album name is primarily comprised
        of letters, numbers, and select special characters
        """
        if (("." not in booktitle) and (booktitle.replace('.','')).isalnum()) and len(booktitle) > 0 or ((" " not in booktitle) and (booktitle.replace(' ','')).isalnum()) > 0 or ((" " not in booktitle) and (booktitle.replace(' ','')).isalnum()) > 0:
            return True
        else:
            print(f"Sorry, but \'{booktitle}\', is invalid! Please try again!")
            return False
    def validate_number_of_chapters(self, number_of_chapters):
        """
        Creating a method to validate a number that 
        someone enters in for the number of chapters in a book.
        """
        if (("." not in number_of_chapters) and (number_of_chapters.replace('.','')).isdigit()):
            return True
        else:
            print(f"Sorry, but \'{number_of_chapters}\', is invalid! Please try again!")
            return False
    def validate_number_of_pages(self,numberOfPages):
        """
        Creating a method to validate the number of pages in a book.
        """
        if numberOfPages.isdigit():
            return True
        else:
            print(f"Sorry, but \'{numberOfPages}\', is invalid! Please try again!")
            return False
    def validate_publication_date(self,publicationdate):
        """
        Creating a method to validate the publication date entered.
        """
        if (("." not in publicationdate) and (publicationdate.replace('.','')).isdigit()) or (("," not in publicationdate) and (publicationdate.replace(',','')).isdigit()):
            return True
        else:
            print(f"Sorry, but \'{publicationdate}\', is invalid! Please try again!")
            return False