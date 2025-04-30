const fs = require('fs');
const path = require('path');


function printTree(dirPath, level = 0) {
    const items = fs.readdirSync(dirPath);

    items.forEach(item => {
        const fullPath = path.join(dirPath, item);
        const stats = fs.statSync(fullPath);


        if (stats.isDirectory()) {

            console.log(' '.repeat(level * 2) + item);


            if (level === 0) {
                printTree(fullPath, level + 1);
            }
        }
    });
}


const rootDir = path.join(__dirname);
printTree(rootDir);
