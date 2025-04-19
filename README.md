# Image Matching with SIFT

**Mini-project by:**
* Alamir Hossam 120210301
* Salma Noureddin 120210389

`ObjectDetection.py`:
1. Loads `query.jpg` (the object we're looking for)
2. Loads `target.jpg` (the larger image where the object may be found)
3. Detects & matches keypoints using SIFT
4. Filters matches using Lowe's ratio test
5. Computes a homography if enough good matches are found
6. Draws a green polygon around the detected object in the target image

## === Example Usage ===
(Place `query.jpg` and `target.jpg` in the same directory as the script)

`query.jpg`: ![query](https://github.com/user-attachments/assets/962ace95-8771-4035-b2b8-e20c0c8bea7d)


`target.jpg`: ![target](https://github.com/user-attachments/assets/1cdb7ddc-8592-4a01-8b52-abd7faa11e61)


`Detected Object`: ![image](https://github.com/user-attachments/assets/28d9cd70-abc3-491a-bde4-6e4d95a5bf83)
