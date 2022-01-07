<?php include $_SERVER['DOCUMENT_ROOT']."/db.php" ?>
<!DOCTYPE HTML>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <meta charset="utf-8">
    <title>TEST COMMUNITY</title>
</head>
<body>
    <div class="container">
        <H1>TEST</H1>
        <table class="table table-hover table-striped text-center">
            <thead>
            <tr>
                <th>번호</th>
                <th>제목</th>
                <th>작성자</th>
                <th>날짜</th>
                <th>조회수</th>
            </tr>
            </thead>
            <?php
                $sql = mq("select * from board order by idx desc limit 5");
                while($board = $sql->fetch_array()){
                    $title=$board["title"];
                    if(strlen($title)>30){
                        $title=str_replace($board["title"],mb_substr($board["title"],0,30,"utf-8")."...",$board["title"]);
                }
            ?>
            <tbody>
            <tr>
                <td><?php echo $board['idx']; ?></td>
                <td><a href="/TtukTtak-Site/read.php?idx=<?php echo $board["idx"]; ?>"><?php echo $title; ?></a></td>
                <td><?php echo $board['name'] ?></td>
                <td><?php echo $board['date'] ?></td>
                <td><?php echo $board['hit'] ?></td>
            </tr>
            </tbody>
            <?php } ?>
        </table>
        <hr/>
        <div id="button">
            <a href="write.php" class="btn btn-outline-primary">글쓰기</a>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>