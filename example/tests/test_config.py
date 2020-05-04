def test_get_config_aws_load(mocker):
    from example import config

    AWSSource = mocker.patch.object(config, "AWSSource", return_value={"custom_key": "custom_value"})
    mocker.patch.object(config, "_app_config", None)

    config = config.get_config({"env": "testing"})

    AWSSource.assert_called_once_with("example/testing")
    assert config["custom_key"] == "custom_value"
