Want your photo instead of the "IUI" monogram on the home page?

1. Drop a square-ish photo in this folder named exactly:  profile.jpg
2. In Home.py, find the line with  <div class="medallion">IUI</div>
   and replace it with:
       <div class="medallion"><img src="app/static/profile.jpg"></div>
3. Move profile.jpg into a folder named  static/  at the repo root
   (Streamlit serves files placed there at the URL app/static/<filename>).

That's it — commit and push, and the app updates automatically.
