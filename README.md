# CBZ

A Python script to convert a directory of images to a CBZ comicbook file.

## Usage

`python cbz.py path/to/image/directory` it will ask you for a comic name. **DO NOT INCLUDE A TRAILING SLASH IN THE PATH OTHERWISE IT WON'T DETECT THE CHAPTER NAME.**

## UltraCBZ

Ultra CBZ should only be used if you have a directory structure like this:

```
Series Name
    Chapter 1
        0.jpg
        1.jpg
        ...
    Chapter 2
        0.jpg
        1.jpg
        ...
    ...
```

It loops through all the chapter directories and converts them to CBZ format.

## Notes

Converted files are stored in the current working directory.