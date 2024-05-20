
"""
Salam , hərvaxtınız xeyir. 2 taskınız olacaq . İlk olaraq dünənki folderlərlə bağlı bir taskımız var. 
İkincisi  isə alqoritmik bir task olacaq.

Folder taskı

1) Ilk olaraq bir "Example" adında bir kateqoriya (directory) yaradırıq.
2)Daha sonra isə bu directorynin içərisində bir  "subdirect"  
adında alt kateqoriya(subdirectory) yaradırıq.
3)Növbəti addımda bu subdirectorynin içərisinə  bir şəkil və bir text faylı əlavə edirik. 
(şəkli ilk öncə manual olaraq hal hazırda olduğunuz qovluğun içərisinə sürüşdürüb  
daha sonra alt kateqoriyaya əlavə edin, path-ini tapmağda çətinlik çəkməmək üçün)
4)daha sonra isə subdirectorynin içərisində olub sonu txt ilə bitən faylları subdirectorydən 
çıxarıb Example directory-sinə göndərirsiniz.


"""


import os
import shutil


if os.path.exists('Example'):
    shutil.rmtree('Example')




example_dir = "Example"
os.makedirs(example_dir, exist_ok=True)



#  "Example" qovluğunun içərisində "subdirect" adlı alt qovluq 
subdirect_dir = os.path.join(example_dir, "subdirect")
os.makedirs(subdirect_dir, exist_ok=True)



# Fayl yolları
current_dir = os.getcwd()
image_src = os.path.join(current_dir, 'image.jpg')
text_src = os.path.join(current_dir, 'file.txt')
image_dst = os.path.join(subdirect_dir, 'image.jpg')
text_dst = os.path.join(subdirect_dir, 'file.txt')



# Sınaq üçün şəkil və mətn 
with open(image_src, 'wb') as img_file:
    img_file.write(os.urandom(1024))  
    # 1KB təsadüfi data




with open(text_src, 'w') as txt_file:
    txt_file.write("Bu, nümunə mətn faylıdır.")


shutil.copy(image_src, image_dst)
shutil.copy(text_src, text_dst)


#  "subdirect" qovluğundakı .txt fayllarını "Example" qovluğuna köçürmek
for file_name in os.listdir(subdirect_dir):
    if file_name.endswith('.txt'):
        src_file = os.path.join(subdirect_dir, file_name)
        dest_file = os.path.join(example_dir, file_name)
        shutil.move(src_file, dest_file)

# yoxlayın
example_files = os.listdir(example_dir)
subdirect_files = os.listdir(subdirect_dir)

print("Example qovluğundakı fayllar:", example_files)
print("subdirect qovluğundakı fayllar:", subdirect_files)
