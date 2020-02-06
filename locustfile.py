from locust import HttpLocust, TaskSet, task, between


class UserBehavior(TaskSet):
    """TaskSetはタスクを集めたクラス"""

    # タスクの実行頻度の重み付け（デコレーションでも可能）
    # tasks = {index: 3, foo: 1}

    def on_start(self):
        """開始時に必ず実行される処理"""
        pass

    def on_stop(self):
        """終了時に必ず実行される処理"""
        pass

    @task(3)  # デコレーションにより実行頻度を指定
    def index(self):
        self.client.get("/")

    @task(1)
    def foo(self):
        pass


class WebsiteUser(HttpLocust):
    """HttpLocustはユーザを表すクラス"""

    # タスクセットを指定
    task_set = UserBehavior

    # ユーザの待機時間？の範囲を指定
    min_wait = 5000
    max_wait = 9000
    # 以下のような書き方も可能、他にも任意の関数が使用可
    # wait_time = between(5, 9)
