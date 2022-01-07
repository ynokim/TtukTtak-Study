<?php
    include $_SERVER['DOCUMENT_ROOT']."/db.php";

    $bno = $_GET['idx'];
    $sql = mq("DELETE FROM board WHERE idx='$bno';");
?>
<script type="text/javascript">alert("해당 글의 삭제가 완료되었습니다.");</script>
<meta http-equiv="refresh" content="0 url=/TtukTtak-Site/index.php" />
