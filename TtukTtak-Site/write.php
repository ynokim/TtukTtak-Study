<!DOCTYPE HTML>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <meta charset="utf-8">
    <title>게시글 작성</title>
</head>
<body>
    <div class="container">
        <h1>WRITE SOMETHING</h1>
        <br>
        <form action="/TtukTtak-Site/check_write.php" method="post">
            <div id="wr_title" class="form-group">
                <label for="title">제목</label>
                <input type="text" class="form-control" id="title" name="title" placeholder="여기에 제목 입력">
            </div>
            <br>
            <div id="wr_writer" class="form-group">
                <label for="writer">작성자</label>
                <input type="text" class="form-control" id="writer" name="writer" placeholder="여기에 작성자 입력">
            </div>
            <br>
            <div id="wr_content" class="form-group">
                <label for="content">글 내용</label>
                <textarea class="form-control" id="content" name="content" placeholder="여기에 글 작성"></textarea>
            </div>
            <br>
            <div id="wr_password" class="form-group">
                <label for="password">비밀번호</label>
                <input type="password" class="form-control" id="password" name="password" placeholder="여기에 게시글 보호용 비밀번호 입력">
            </div>
            <br>
            <div id="wr_submit_button">
                <button type="submit" class="btn btn-outline-primary">글 작성</button>
            </div>
        </form>
    </div>




    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>