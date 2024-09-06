require "yast/rake"

Yast::Tasks.submit_to :sle15sp7

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end

desc "Generate the QSS and CSS files"
task :generate do
  unless system("which npm >/dev/null 2>&1")
    abort "Error: The npm package is not installed, install it with command " \
      "\"zypper install npm-default\""
  end

  Dir.chdir("src") do
    system("npm install") unless File.exist?("node_modules")
    system("npx gulp")
  end
end

# support for the "yupdate" tool when running in the inst-sys
if File.exist?("/.packages.initrd")
  # redefine the "install" task
  Rake::Task["install"].clear
  task :install do
    # prepare the target directories
    destdir = ENV["DESTDIR"] || "/"
    icewm_dir = File.join(destdir, "/etc/icewm/")
    theme_dir = File.join(destdir, "/usr/share/YaST2/theme/current/")
    FileUtils.mkdir_p(icewm_dir)
    FileUtils.mkdir_p(theme_dir)

    # SLE or openSUSE installation?
    sle = File.read("/etc/os-release").match?(/SUSE Linux Enterprise/i)
    theme = sle ? "SLE" : "openSUSE"

    # copy the theme files, the "/." at the end of the source directory
    # means copy all files from that directory
    FileUtils.cp_r("theme/#{theme}/wmconfig/.", icewm_dir)
    FileUtils.cp_r("theme/#{theme}/.", theme_dir)
  end
end
