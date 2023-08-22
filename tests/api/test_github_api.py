import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")

    assert r["total_count"] >= 43


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")

    assert r["total_count"] != 0


@pytest.mark.api
def test_valid_object_url(github_api):
    r = github_api.search_emojis()

    assert (
        r["+1"]
        == "https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8"
    )


@pytest.mark.api
def test_invalid_object_url(github_api):
    r = github_api.search_emojis()

    assert (
        r["100"]
        != "https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8"
    )


@pytest.mark.api
def test_number_of_dictionary_items(github_api):
    r = github_api.search_emojis()

    assert len(r) == 1877


@pytest.mark.api
def test_key_is_present(github_api):
    r = github_api.search_emojis()

    assert "angel" in r


@pytest.mark.api
def test_checking_a_list_item(github_api):
    r = github_api.get_commits("NazariiKhymyn", "KhymynQAauto")

    assert r[0]["sha"] == "64697be29535d7199a78ea5ebd6faa4684068f9d"


@pytest.mark.api
def test_checking_mail_author_commit(github_api):
    r = github_api.get_commits("NazariiKhymyn", "KhymynQAauto")

    assert r[0].get("commit").get("author").get("email") == "mizuna@ukr.net"


@pytest.mark.api
def test_verification_of_login_committer(github_api):
    r = github_api.get_commits("NazariiKhymyn", "KhymynQAauto")

    assert r[0]["committer"]["login"] == "NazariiKhymyn"


@pytest.mark.api
def test_checking_message_commit(github_api):
    r = github_api.get_commits("NazariiKhymyn", "KhymynQAauto")

    assert r[20]["commit"]["message"] == "Modul 26. Project task three"
