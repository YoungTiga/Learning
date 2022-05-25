from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self,pages):
        self.pages = pages
        self.photos = self.__init__photos(pages)

    def __init__photos(self,pages):
        return [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls,photos_count: int):
        pages =ceil(photos_count/PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self,label:str):
        for idx, page in enumerate(self.photos):
            if len(page)< PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {idx+1} slot {len(page)}"
        return "No more free slots"
    def display(self):
        separator = "-" * 11
        result = separator + "\n"
        for page in self.photos:
            # if i % 2 == 1:
            #     result += "-" * 11 + "\n"
            # else:
            result += " ".join("[]" for photo in page) + "\n"
            result += separator
        return result




album = PhotoAlbum(3)
for _ in range(8):
    album.add_photo("asdf")
print(album.display().strip())
