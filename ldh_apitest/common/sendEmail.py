'pljigzgwrztkbdhb'

import smtplib
smtp=smtplib.SMTP_SSL('smtp.qq.com',465)
smtp.login('616798887@qq.com', 'pljigzgwrztkbdhb')
smtp.sendmail('616798887@qq.com', '56844906@qq.com', 'ss')
smtp.quit()