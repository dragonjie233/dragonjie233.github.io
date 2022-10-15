import os

filepath = './post'
fileurl  = filepath + '/'

List = []

files = os.listdir(filepath)
files.sort(key= lambda x:int(x[:8]))

for file in files:
    fileDate = file.replace('.md', '')

    with open(fileurl + file, "r", encoding="utf-8") as f:
        title = f.readline().rstrip().replace('# ', '')
        title2html = '<a href="%s"><i>%s月%s日</i>%s</a>\n' % (fileurl + file, fileDate[4:6], fileDate[6:8], title)

    List.append('            ' + title2html)
    List.append('\n            <h2>' + fileDate[0:4] + ' 年</h2>\n')

List.reverse()
print(List)
postList = list(set(List))
postList.sort(key=List.index)

html1 = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LongJie&ensp; : )</title>
    <meta name="robots" content="index,follow"/>
    <meta name="author" content="LongJie"/>
    <meta name="description" content="好记性不如烂笔头。"/>
    <meta name="keywords" content="longjie,longjie blog,龙介,龙介博客"/>
    <link rel="stylesheet" href="static/style.css">
    <link rel="stylesheet" href="https://cdn.staticfile.org/highlight.js/11.6.0/styles/atom-one-light.min.css">
</head>
<body>
    <main class="container">
        <div id="load" class="list">'''
html2 = '''        </div>
    </main>
    <script src="https://cdn.staticfile.org/marked/2.1.3/marked.min.js"></script>
    <script src="https://cdn.staticfile.org/highlight.js/11.6.0/highlight.min.js"></script>
    <script src="static/script.js"></script>
</body>
</html>'''

html = html1 + ''.join(postList) + html2

output = open('index.html', 'w+', encoding="utf-8")
output.write(html)
output.flush()
output.close()



