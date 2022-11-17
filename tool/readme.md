# 工具类的使用

## MinioHelper

1. 连接&初始化

```python
import tool
import config

minioClient = tool.MinioHelper.MinioHelper(config.MinioPath,
                                           config.MinioPort,
                                           config.MinioAccount,
                                           config.MinioPassword,
                                           config.MinioBucket)
minioClient.setConnection()
```

如果连接失败，将直接exit。

所有默认参数都在[`config.py`](config.py)中。

2. `def uploadFileByUrl(self, name)`

参数name是上传文件的名字。调用后，将返回一个链接，使用`put`方法上传二进制文件。

```python
import requests
import tool
import config

minioClient = tool.MinioHelper.MinioHelper(config.MinioPath,
                                           config.MinioPort,
                                           config.MinioAccount,
                                           config.MinioPassword,
                                           config.MinioBucket)
minioClient.setConnection()
filePath = "./README.md"
with open(filePath, 'rb').read() as f:
   url = minioClient.uploadFileByUrl("README.md")
   requests.put(url, data=f)
```

3. `def downloadFileByUrl(self, name)`
   参数name是下载文件的名字。调用后，将返回一个链接，使用`get`方法下载二进制文件。

```python
import requests
import tool
import config

minioClient = tool.MinioHelper.MinioHelper(config.MinioPath,
                                           config.MinioPort,
                                           config.MinioAccount,
                                           config.MinioPassword,
                                           config.MinioBucket)
minioClient.setConnection()
filePath = "./README.md"
with open(filePath, 'wb') as f:
   url = minioClient.downloadFileByUrl("README.md")
   binFile = requests.get(url).content
   f.write(binFile)
```

## Model&Service

## SqliteHelper

## ThreadingHelper

## Tools

## VideoHelper