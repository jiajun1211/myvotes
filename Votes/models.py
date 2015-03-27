from django.db import models

# Create your models here.
# @property(readonly, nonatomic,assign) NSUInteger vid;
# @property(readonly, nonatomic,copy) NSString *uname;
# @property(readonly, nonatomic,copy) NSURL *uimg;
# @property(readonly, nonatomic,copy) NSString *name;
# @property(readonly,nonatomic,copy)NSString *title;
# @property(readonly,nonatomic,copy)NSString *leftItemText;
# @property(readonly,nonatomic,copy)NSString *reghtItemText;
# @property(readonly,nonatomic,copy)NSURL *leftItemImg;
# @property(readonly,nonatomic,copy)NSURL *rightItemImg;
# @property(readwrite,nonatomic,assign)NSInteger leftCount;
# @property(readwrite,nonatomic,assign)NSInteger rightCount;
# @property(readwrite,nonatomic,assign)BOOL leftSelected;
# @property(readwrite,nonatomic,assign)BOOL rightSelected;
class Vote(models.Model):

    u_name = models.CharField(max_length=100)
    u_img = models.URLField()
    v_name = models.CharField(max_length=200)
    v_title = models.CharField(max_length=200)
    v_leftItemText = models.CharField(max_length=200)
    v_rightItemText = models.CharField(max_length=200)
    v_leftItemImg = models.URLField()
    v_rightItemImg = models.URLField()
    v_leftCount = models.IntegerField()
    v_rightCount = models.IntegerField()

    def to_json(self):
        return {'u_name': self.u_name,
                'u_img': self.u_img,
                'v_name': self.v_name,
                'v_title': self.v_title,
                'v_lit': self.v_leftItemText,
                'v_rit': self.v_rightItemText,
                'v_lii': self.v_leftItemImg,
                'v_rii': self.v_rightItemImg,
                'v_lc': self.v_leftCount,
                'v_rc': self.v_rightCount,
                }



