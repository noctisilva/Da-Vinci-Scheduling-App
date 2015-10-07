VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network "forwarded_port", guest: 8080, host: 8080
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.hostname = "dev"
    config.vm.provision "shell", path: "provisioning/core.sh", privileged: false

    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
    end
end
