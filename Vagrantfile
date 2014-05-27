# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
 
 config.vm.define "vagrant-ubuntu2" do |v|
  v.vm.provider "docker" do |d|
    #d.image = "guilhem/vagrant-ubuntu"
    d.build_dir = "."
    d.has_ssh = true
  end

  # Specify SSH info
  #v.ssh.username = "root"
  #v.ssh.private_key_path = "insecure_key"
  
 # v.vm.provision "shell", inline: "echo Hello"
  #v.vm.synced_folder "./keys", "/vagrant"
  #if File.exists?("projects")
  #  config.vm.synced_folder "projects", "/home/vagrant/projects"
  #end
  v.vm.synced_folder "projects", "/home/vagrant/projects"
 end
end
