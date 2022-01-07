<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";
?>

<!DOCTYPE HTML>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <meta charset="utf-8">
    <title>TEST COMMUNITY</title>
</head>
<body>
    <?php
    $bno = $_GET['idx']; /* bno함수에 idx값을 받아와 넣음*/
    $hit = mysqli_fetch_array(mq("select * from board where idx ='".$bno."'"));
    $hit = $hit['hit'] + 1;
    $fet = mq("update board set hit = '".$hit."' where idx = '".$bno."'");
    $sql = mq("select * from board where idx='".$bno."'"); /* 받아온 idx값을 선택 */
    $board = $sql->fetch_array();
    ?>
    <div class="container">
        <h1><?php echo $board['title']; ?></h1>
        <div id="info">
            글쓴이: <?php echo $board['name']; ?> <br> 작성일: <?php echo $board['date']; ?> <br> 조회: <?php echo $board['hit']; ?>
        </div>
        <br>
        <div id="contents">
            <?php echo nl2br("$board[content]"); ?>
        </div>
        <br>
        <div id="bottom">
            <ul style="list-style: none; padding-left: 0px;">
                <li><a href="/TtukTtak-Site/index.php" class="btn btn-outline-primary">목록으로</a></li>
                <li><a href="/TtukTtak-Site/modify.php?idx=<?php echo $board['idx']; ?>" class="btn btn-outline-primary">수정하기</a></li>
                <li><a href="/TtukTtak-Site/delete.php?idx=<?php echo $board['idx']; ?>" class="btn btn-outline-primary">삭제하기</a></li>
            </ul>
        </div>
    </div>
</body>
