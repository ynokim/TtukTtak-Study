<?php
    include $_SERVER['DOCUMENT_ROOT']."/db.php";

    $bno = $_GET['idx'];
    $sql = mq("SELECT * FROM board WHERE idx='$bno';");
    $board = $sql -> fetch_array();
?>

<!DOCTYPE HTML>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <meta charset="utf-8">
    <title>게시글 작성</title>
</head>
<body>
<div class="container">
    <h1>MODIFY SOMETHING</h1>
    <br>
    <form action="/TtukTtak-Site/check_modify.php?idx=<?php echo $bno; ?>" method="post">
        <div id="wr_title" class="form-group">
            <label for="title">제목</label>
            <input type="text" class="form-control" id="title" name="title" placeholder="<?php echo $board['title']; ?>">
        </div>
        <br>
        <div id="wr_writer" class="form-group">
            <label for="writer">작성자</label>
            <input type="text" class="form-control" id="writer" name="writer" placeholder="<?php echo $board['name']; ?>">
        </div>
        <br>
        <div id="wr_content" class="form-group">
            <label for="content">글 내용</label>
            <textarea class="form-control" id="content" name="content" placeholder="<?php echo $board['content']; ?>"></textarea>
        </div>
        <br>
        <div id="wr_password" class="form-group">
            <label for="password">비밀번호</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="여기에 게시글 보호용 비밀번호 입력">
        </div>
        <br>
        <div id="wr_submit_button">
            <button type="submit" class="btn btn-outline-primary">글 수정</button>
        </div>
    </form>
</div>




<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>