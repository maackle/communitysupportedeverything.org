module.exports = (grunt) ->

	grunt.initConfig

		paths:
			src: "assets"
			dest: "static"

		pkg: grunt.file.readJSON("package.json")

		watch:
			livereload:
				files: [
					"<%= paths.dest %>/{,**}/*.css"
					# "<%= paths.templates %>/**/*"
				]
				options:
					livereload: 7331
			#js:
			#	files: ["<%= paths.src %>/scripts/{,**}/*.coffee"]
			#	tasks: ["coffee"]
			less:
				files: ["<%= paths.src %>/styles/{,**}/*.less"]
				tasks: ["less"]


		coffee:
			compile:
				options:
					join: true
				files: [
					"<%= paths.dest %>/build/main.js": [
						"<%= paths.src %>/scripts/*.coffee"
					]
				]


		less:
			development: 
				options: 
					paths: ["<%= paths.src %>/style"]
				files: 
					"<%= paths.dest %>/build/bootstrap.css": "<%= paths.src %>/styles/bootstrap.less"


	grunt.loadNpmTasks("grunt-contrib-coffee")
	grunt.loadNpmTasks("grunt-contrib-less")
	grunt.loadNpmTasks("grunt-contrib-connect")
	grunt.loadNpmTasks("grunt-contrib-watch")
	grunt.loadNpmTasks("grunt-contrib-compass")
	grunt.loadNpmTasks("grunt-shell")
	grunt.loadNpmTasks("grunt-concurrent")
	grunt.loadNpmTasks("grunt-notify")

	# grunt.registerTask "server", ['shell:flask']

	grunt.registerTask "default", [
		'coffee'
		'less'
		# 'compass'
		# 'connect'
		'watch'
	]

# npm install --save-dev \
# grunt \
# grunt-contrib-coffee \
# grunt-contrib-connect \
# grunt-contrib-watch \
# grunt-contrib-compass \
# grunt-contrib-copy \
# grunt-notify