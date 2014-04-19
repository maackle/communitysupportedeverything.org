module.exports = (grunt) ->

	grunt.initConfig

		paths:
			src: "src"
			dest: "public"

		pkg: grunt.file.readJSON("package.json")

		watch:
			livereload:
				files: [
					"<%= paths.dest %>/assets/{,**}/*.css"
					# "<%= paths.templates %>/**/*"
				]
				options:
					livereload: 7331
			#js:
			#	files: ["<%= paths.src %>/scripts/{,**}/*.coffee"]
			#	tasks: ["coffee"]
			less:
				files: ["<%= paths.dest %>/assets/style/{,**}/*.less"]
				tasks: ["less"]

		connect:
			server:
				options:
					open: true
					livereload: 7331
					port: 1337
					base: '<%= paths.dest %>'


		coffee:
			compile:
				options:
					join: true
				files: [
					"<%= paths.dest %>/assets/build/main.js": [
						"<%= paths.src %>/scripts/*.coffee"
					]
				]


		compass:
			dist:
				options:
					noLineComments: false
					# debugInfo: true
					# bundleExec: true
					sassDir: '<%= paths.src %>/styles'
					cssDir: '<%= paths.dest %>/assets/build'
					environment: 'development'
					require: [

					]

		less:
			development: 
				options: 
					paths: ["<%= paths.dest %>/assets/style"]
				files: 
					"<%= paths.dest %>/assets/build/bootstrap.css": "<%= paths.dest %>/assets/style/bootstrap.less"


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
		'connect'
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