<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";

$bno = $_GET['idx'];
$username = $_POST['writer'];
$userpw = password_hash($_POST['pw'], PASSWORD_DEFAULT);
$title = $_POST['title'];
$content = $_POST['content'];
$sql = mq("UPDATE board SET name='".$username."',pw='".$userpw."',title='".$title."',content='".$content."' WHERE idx='".$bno."'"); ?>

<script type="text/javascript">alert("게시글 수정이 완료되었습니다."); </script>
<meta http-equiv="refresh" content="0 url=/TtukTtak-Site/read.php?idx=<?php echo $bno; ?>">