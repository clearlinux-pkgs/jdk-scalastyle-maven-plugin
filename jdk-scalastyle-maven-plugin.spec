Name     : jdk-scalastyle-maven-plugin
Version  : 0.8.0
Release  : 1
URL      : http://repo1.maven.org/maven2/org/scalastyle/scalastyle-maven-plugin/0.8.0/scalastyle-maven-plugin-0.8.0.jar
Source0  : http://repo1.maven.org/maven2/org/scalastyle/scalastyle-maven-plugin/0.8.0/scalastyle-maven-plugin-0.8.0.jar
Source1  : http://repo1.maven.org/maven2/org/scalastyle/scalastyle-maven-plugin/0.8.0/scalastyle-maven-plugin-0.8.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/scalastyle-maven-plugin.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/scalastyle-maven-plugin.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/scalastyle-maven-plugin.xml \
%{buildroot}/usr/share/maven-poms/scalastyle-maven-plugin.pom \
%{buildroot}/usr/share/java/scalastyle-maven-plugin.jar \

%files
%defattr(-,root,root,-)
/usr/share/java/scalastyle-maven-plugin.jar
/usr/share/maven-metadata/scalastyle-maven-plugin.xml
/usr/share/maven-poms/scalastyle-maven-plugin.pom
