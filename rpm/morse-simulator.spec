
Name:          morse-simulator
Version:       1.4
Release:       1%{?dist}
Summary:       Multi-OpenRobot Simulation Engine
License:       BSD
URL:           https://morse-simulator.github.io/

Source0:       https://github.com/morse-simulator/morse/archive/%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-numpy
Requires:      python3
Requires:      python3-numpy
Requires:      blender


%description
 List of morse features:
  * Versatile simulator for generic mobile robots simulation
    (single or multi robots),
  * Realistic and dynamic environments (interaction with other agents like
    humans or objects),
  * Based on well known and widely adopted open source projects (Blender for 3D
    rendering + UI, Bullet for physics simulation, dedicated robotic
    middlewares for communications + robot hardware support),
  * Seamless workflow: since the simulator rely on Blender for both modeling
    and the real time 3D engine, creating and modifying a simulated scene is
    straightforward.
  * Entirely scriptable in Python,
  * Adaptable to various level of simulation realism (for instance the
    simulation of exteroceptive sensors like cameras or a direct access to
    higher level representations of the world, like labeled artifacts),
  * Currently compatible with ROS, YARP and the LAAS OpenRobots robotics
    frameworks,
  * Easy to integrate to other environments via a simple socket interface,
  * Fully open source, BSD license.
  
%prep
%setup -q -n morse-%{version}

%build
mkdir cmake-make
pushd cmake-make
%cmake ..
%make_build
popd

%install
pushd cmake-make
%make_install
popd

%files -f cmake-make/install_manifest.txt
%{_datadir}/morse/*
%{python3_sitearch}/morse/*
%{python3_sitearch}/pymorse/*


%changelog
* Mon Aug 06 2018 Rafael Bailon-Ruiz <rafael.bailon-ruiz@laas.fr> - 1.4-1
- Initial package
