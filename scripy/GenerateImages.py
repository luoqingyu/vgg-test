# -*- coding: UTF-8 -*-
import  os
import  random
import PIL.Image as Image
class GenerateImages:
    def __init__(self,pic_size=['32','256'],max_word_num=8,src_path='',out_path='',if_random_space='False',random_space=[0,0],space=0):
        self.pic_size = pic_size
        self.max_word_num = max_word_num
        self.src_path = src_path
        self.out_path = out_path
        self.if_random_space = if_random_space
        self.random_space = random_space
        self.space=space

        print if_random_space




    def readEachFile(self,read_path):
        pathDir = os.listdir(read_path)
        Absolute_dir = []
        name_list = []
        for allDir in pathDir:

            child = os.path.join('%s%s' % (read_path, allDir))
            # print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
            Absolute_dir.append(child)
            name_list.append(allDir)
        return Absolute_dir, name_list





    def creatPic(self,num='1000'):
        A_path,na_list = self.readEachFile(read_path=self.src_path)
        img_list = []
        for child_list in A_path:
            img,name = self.readEachFile(child_list+'/')
            img_list.append(img)

        txtName = self.out_path+"word_list.txt"
        f = file(txtName, "w")


        for num in range(num):
            toImage = Image.new('RGBA', (256, 32), (255, 255, 255))
            name = ''
            for i in range(self.max_word_num):
                zi = random.randrange(0, len(img_list))             #选择字
                if (zi < len(img_list)):
                    ziti = random.randrange(0, len(img_list[zi]))    #选择字体
                    name = name + img_list[zi][ziti].split("/")[-2]  #获取字的编码

                    # x =  random.randrange(0, len(list))
                    fromImage = Image.open(img_list[zi][ziti])
                    fromImage = fromImage.resize((32, 32), Image.ANTIALIAS)  # 先拼的图片不多，不用缩小

                    if (self.if_random_space==True):
                        self.space = random.randrange(self.random_space[0],self.random_space[1])
                        #print (self.space)
                    print (self.space)
                    toImage.paste(fromImage, ((i) * 32+(self.space), 0))

            toImage.save(self.out_path + name + '.png')
            f.write(name+'.png'+' '+name+'\n')
        f.close()

if __name__ == '__main__':
    x= GenerateImages(src_path='/home/lqy/project/OCR/ocr_cnn_lstm_ctc/data/danzi-test/',
                      out_path='/home/lqy/project/OCR/ocr_cnn_lstm_ctc/data/test/',
                      if_random_space = True,
                      random_space=[-15,15],
                      space=0)
    x.creatPic(num=100)


