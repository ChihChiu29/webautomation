# A collection of web automation libs and examples.

## Examples

All commands are assumed to be run from root directory.

### Google slides screenshoter

Usage:

```
python -m fetcher.google_slides --url='<slides url, in presentation mode>' --num_of_pages=<number of pages>
```

Once done, screenshots will appear under `data` folder, then you can join them into a pdf using:

```
convert *.png foo.pdf
```
