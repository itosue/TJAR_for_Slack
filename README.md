# TJAR_for_Slack
TJAR - Throw JSON After Rendering. 

This addon throws JSON webhook to Slack after rendering. You don't need to check whteher rendering is finished or not anymore.
You can send notification to any device via slack.(I get notifications from Pebble via SlackApp.) 

This addon sends 2 messages.  
1)render canceled : This will be sent when rendering is canceled (ex.closing window etc...)
2)render completed : This will be sent end when rendering is completed.

Message customization is now work in progress. I left the codes as comment so use it if you want.
I wrote this as simple JSON sender so you may tweak this code for other services easily.(ex. Just Changing URL&JSON body and it might adopts IFTTT's Maker etc...)


日本語ヘルプ  
Render終了時にSlackへMessageを投げるスクリプトです。
一晩かかるレンダリングならすぐに諦めて寝たりできますが、15分や20分等、中途半端なレンダリング時間だと、終わったかどうか気になってチラチラ見ては「まだか〜〜〜〜」ってがっかりするのに懲りたので作ってみました。

もっと汎用的にJSONを投げるアドオンにしたかったのですが、時間が無いのでとりあえずSlack特化でリリースします。
ちょっとコード読める人なら簡単に改造できると思いますので、色々いじってみてください。（URLとJSONのコードの部分を変えたらIFTTT用とかにすぐ改造できると思います。）私はSlack→SlackのAndroidApp→Notification→Pebbleという感じで、通知を受け取るようにしています。

投げられるメッセージ  
1)レンダーがキャンセルされた時（Windowが閉じられた時など）  
2)レンダー（若しくはアニメーション）出力完了時  

メッセージのカスタマイズも実装しようとしたのですが、中途半端になったので切り捨てました。
カスタマイズしたい人はコードの中にコメントで残してますので、適宜改造して動かして下さい。
初めてのPythonのコード＆Blenderのライブラリなので、変なとこもあるかもですが、ご容赦下さいm(_ _)m
