<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";

$user_name = $_POST['writer'];
$user_pw = password_hash($_POST['password'], PASSWORD_DEFAULT);
$title = $_POST['title'];
$content = $_POST['content'];
$date = date('Y-m-d');
$hit = 0;

if($user_name && $user_pw && $title && $content){
    $sql = mq("INSERT INTO board(name, pw, title, content, date, hit) values('".$user_name."','".$user_pw."','".$title."','".$content."','".$date."', '".$hit."')");
    echo "<script>alert('글쓰기가 완료되었습니다'); location.href='/TtukTtak-Site/index.php';</script>";
}
else{
    echo "<script>alert('글쓰기에 실패하였습니다.'); history.back()</script>";
}