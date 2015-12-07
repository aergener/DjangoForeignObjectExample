# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://atlas.hashicorp.com/ubuntu/boxes/trusty64"

  config.vm.network "forwarded_port", guest: 8000, host: 8888

  config.vm.provision :shell, path: "provision.sh", args: "foreignobject"

  config.vm.synced_folder '.', '/home/vagrant/app/'
end
