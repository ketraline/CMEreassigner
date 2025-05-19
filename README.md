# CMEreassigner
A small script that recolors sprites based on a color map.
## Use
This script requires 3 files - an image displaying all of the correct colors, a map image with a color assigned to each pixel that should be sampled and an exit image made with the colors in the map.
For files called Color.png, Map.png and Exit.png, the command should be:
`python CMEreassigner.py Color.png Map.png Exit.png`
## Example
Let's say this is our colored image:
![Color](https://github.com/user-attachments/assets/aa0e3f79-d668-4f3c-aedf-75cc28d31336)

This is the map of that image:
![Map](https://github.com/user-attachments/assets/e105ddf5-91aa-42ea-8f87-37fd960cd5a4)

And this is the image we want to color:
![Edit](https://github.com/user-attachments/assets/04362f3c-e92c-4e40-aa82-a8991cad9387)

The output will look like this.
![Exit](https://github.com/user-attachments/assets/7d1c0e30-455f-4dc8-b2f7-6bb996c4e2e5)
