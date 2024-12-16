import allure


class Endpoint:

    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_status_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that response is 404')
    def check_status_404(self):
        assert self.response.status_code == 404
